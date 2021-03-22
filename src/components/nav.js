import React from "react";
import PropTypes from "prop-types";

export const Nav = ({ style }) => {
  return (
    <section className="bb fixed dt w-100 cf" style={style}>
      <nav className="pl4 tracked">
        <div className="flex flex-wrap">
          <div className="w-100 w-third-ns">
            <h1 className="bl bw2 f5 pl1 mb0">Kim Kopowski</h1>
          </div>
        </div>
        <div className="mv1 f6">
          <a
            href="mailto:kim.kopowski@gmail.com"
            className="db link dim"
            style={style}
          >
            kim.kopowski@gmail.com
          </a>

          <a href="tel:+15033880601" className="db link dim" style={style}>
            1-503-388-0601
          </a>
        </div>
      </nav>
    </section>
  );
};

Nav.propTypes = {
  style: PropTypes.object,
};
