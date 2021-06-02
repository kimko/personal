import React from "react";
import PropTypes from "prop-types";

export const Info = ({ title, text, setShowInfo }) => {
  return (
    <>
      <section>
        <article className="mw8 center br2 ba b--hot-pink bg-pink">
          <div className="dt-ns dt--fixed-ns w-100">
            <div className="pa3 pa4-ns dtc-ns v-mid">
              <div>
                <h2 className="fw4 mt0 mb3">{title} </h2>
                <p className="black-70 measure lh-copy mv0">
                  {text}
                </p>
              </div>
            </div>
            <div className="pa3 pa4-ns dtc-ns v-mid">
              <button
                onClick={() => setShowInfo(false)}
              >
                OK
              </button>
            </div>
          </div>
        </article>
      </section>
    </>
  );
};

Info.propTypes = {
  title: PropTypes.string,
  text: PropTypes.string,
  setShowInfo: PropTypes.func,
};
