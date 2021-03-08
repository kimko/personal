import React from "react";
import logo from "../logo.svg";

export const Nav = () => {
  return (
    <header class="bg-black-90 fixed w-100 ph3 pv3 pv4-ns ph4-m ph5-l">
      <nav class="f6 fw6 ttu tracked">
      <a className="dtc v-mid mid-gray link dim w-25" href="#" title="Home">
        <img src={logo} className="dib w2 h2 br-100" alt="Site Name" />
      </a>
      <div className="dtc v-mid w-75 tr">
        <a
          className="link dim white f6 f5-ns dib mr3 mr4-ns"
          href="#"
          title="About"
        >
          Services
        </a>
        <a
          className="link dim white f6 f5-ns dib mr3 mr4-ns"
          href="#"
          title="Store"
        >
          Blog
        </a>
        <a className="link dim white f6 f5-ns dib" href="#" title="Contact">
          Join Us
        </a>
      </div>
      </nav>
    </header>
  );
};
