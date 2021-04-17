import React from "react";
import PropTypes from "prop-types";

export const Nav = ({ style, name, email, phone }) => {
  return (
    <section
      className="bb fixed dt w-100 cf"
      style={style}
      data-testid="test-section-nav"
    >
      <nav className="pl4 tracked">
        <div className="flex flex-wrap">
          <div className="w-100 w-third-ns">
            <h1 className="bl bw2 f5 pl1 mb0">{name}</h1>
          </div>
        </div>
        <div className="mv1 f6">
          <a href={`mailto:${email}`} className="db link dim" style={style}>
            {email}
          </a>

          <a href={`tel:${phone.raw}`} className="db link dim" style={style}>
            {phone.pretty}
          </a>
        </div>
      </nav>
    </section>
  );
};

Nav.propTypes = {
  style: PropTypes.object,
  name: PropTypes.string,
  email: PropTypes.string,
  phone: PropTypes.object,
};
