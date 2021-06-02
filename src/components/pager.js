import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";

import { fetchContent, fetchFromUrl } from "./pager_api.js";
import { UserList } from "./pager_user_list.js";
import { UserContent } from "./pager_user_contacts.js";
import { Info } from "./pager_info";

export const Pager = (props) => {
  const [content, setContent] = useState([]);
  const [token, setToken] = useState("y_NbAkKc66ryYTWUXYEu");
  const [info, setInfo] = useState({ title: "", text: "" });
  const [showInfo, setShowInfo] = useState(false);
  // Paging
  const [loading, setLoading] = useState(false);
  const [displayLimit, setDisplayLimit] = useState(6);
  const [contentTotal, setContentTotal] = useState(0);
  const [currentPage, setCurrentPage] = useState(1);

  const [update, toggleUpdate] = useState(false);
  const [newDisplayLimit, setNewDisplayLimit] = useState(6);

  const paginate = (pageNumber) => {
    setCurrentPage(pageNumber);
    setUserName("");
    setUser([]);
  };

  // Show contacts
  const [userUrl, setUserUrl] = useState("");
  const [user, setUser] = useState([]);
  const [userName, setUserName] = useState("");

  // load user list
  useEffect(() => {
    const parameters = {
      offset: currentPage * displayLimit - displayLimit,
      limit: displayLimit,
      total: true,
    };
    fetchContent(
      "users",
      setLoading,
      setContent,
      setContentTotal,
      token,
      setInfo,
      setShowInfo,
      parameters,
    );
  }, [currentPage, update]);

  // load contacts
  useEffect(() => {
    fetchFromUrl(userUrl, "contact_methods", setLoading, setUser, token, setInfo, setShowInfo);
  }, [userUrl]);

  const onButtonClickorInputBlur = () => {
    if (newDisplayLimit > 0 && newDisplayLimit < contentTotal) {
      setDisplayLimit(newDisplayLimit);
      toggleUpdate(!update);
    }
  };
  return (
    <div className="pa4 mw7">
      {showInfo === true && (<Info title={info.title} text={info.text} setShowInfo={setShowInfo} />)}
      <Input
        label="Api token"
        value={token}
        setValue={setToken}
        description={"Test API Token (this key is available to the public)"}
      />
      <Input
        label="Page limit"
        value={newDisplayLimit}
        setValue={setNewDisplayLimit}
        description={"Set pagination limit"}
      />
      <button className="ml2" onClick={onButtonClickorInputBlur}>
        Update
      </button>
      <h3>Users:</h3>
      <UserList
        content={content}
        setUserUrl={setUserUrl}
        setUserName={setUserName}
      />
      {content.length && (
        <Pagination
          limit={displayLimit}
          total={contentTotal}
          paginate={paginate}
          currentPage={currentPage}
        />
      )}
      <h3>{`${userName} Contacts:`}</h3>
      {user.length && <UserContent content={user} />}
      {loading && <h3>Loading...</h3>}
    </div>
  );
};

Pager.propTypes = {
  style: PropTypes.object,
};

const Pagination = ({ limit, total, paginate, currentPage }) => {
  const pageNumbers = [];

  for (let i = 1; i <= Math.ceil(total / limit); i++) {
    pageNumbers.push(i);
  }

  const buttonStyle = (color) => {
    return `f6 link dim ph3 pv2 mt1 mr2 mb2 dib white bg-${color}`;
  };
  return (
    <>
      <small className="f6 black-60 db mb2">{`Showing ${limit} out of ${total}`}</small>
      <nav>
        {pageNumbers.map((number) => (
          <a
            onClick={() => paginate(number)}
            key={number}
            className={buttonStyle(
              number === currentPage ? "hot-pink" : "black",
            )}
          >
            {number}
          </a>
        ))}
      </nav>
    </>
  );
};

Pagination.propTypes = {
  limit: PropTypes.number,
  total: PropTypes.number,
  paginate: PropTypes.func,
  currentPage: PropTypes.number,
};

const Input = ({ label, value, setValue, description }) => {
  return (
    <form className="pa2 black-80">
      <div className="measure">
        <label htmlFor={label} className="f6 b db mb2">
          {label}
          {/* <span className="normal black-60">(optional)</span>*/}
        </label>
        <input
          id={label}
          className="input-reset ba b--black-20 pa2 mb2 db w-100"
          type="text"
          aria-describedby="name-desc"
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
        <small id={`${label}-desc`} className="f6 black-60 db mb2">
          {description}
        </small>
      </div>
    </form>
  );
};

Input.propTypes = {
  label: PropTypes.string,
  value: PropTypes.any,
  setValue: PropTypes.func,
  toggleUpdate: PropTypes.func,
  description: PropTypes.string,
};
