import React from "react";
import PropTypes from "prop-types";

export const UserContent = ({ content }) => {
    return (
        <>
          {content.map((element) => (
            <article key={element.id} className="mw5 mw6-ns br3 hidden ba b--black-10">
                <h1 className="f4 bg-near-white br3 br--top black-60 mv0 pv2 ph3">{element.summary}</h1>
                <div className="bt b--black-10">
                    <p className="f6 f5-ns lh-copy">
                    {element.address}
                    </p>
                </div>
            </article>
          ))}
      </>
    );
  };
  
  UserContent.propTypes = {
    content: PropTypes.array,
  };
