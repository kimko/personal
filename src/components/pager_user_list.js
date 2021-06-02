import React from "react";
import PropTypes from "prop-types";

export const UserList = ({ content, setUserUrl, setUserName }) => {
    const thStyle = "pv2 ph3 tl f6 fw6 ttu";
    const tdStyle = "pv2 ph3";
    const loadAndDisplayContacts = (e) => {
      setUserUrl(e.self + '/contact_methods');
      setUserName(e.name);
    }

    return (
      <table className="collapse ml2 ba br2 b--black-10 pv2 ph3">
        <tbody>
          <tr key="-1" className="striped--light-gray">
            <th className={thStyle}>ID</th>
            <th className={thStyle}>Name</th>
            <th className={thStyle}>Contacts</th>
          </tr>
          {content.map((element) => (
            <tr key={element.id} className="striped--light-gray">
              <td className={tdStyle}>{element.id}</td>
              <td className={tdStyle}>{element.name}</td>
              <td className={tdStyle}><button onClick={() => loadAndDisplayContacts(element)}>Contacts</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  };
  
  UserList.propTypes = {
    content: PropTypes.array,
    setUserUrl: PropTypes.func,
    setUserName: PropTypes.func,
  };
