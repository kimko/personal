import React, { Component, useRef, useEffect } from "react";
import PropTypes from "prop-types";

import { Nav } from "./nav";
import { Summary } from "./cvSummary";
import { Experience } from "./cvExperience";
import { Skills } from "./cvSkills";
import { SocialSimple } from "./footer";
import * as cvContent from "./../content/cv";

export const Cv = (props) => {
  return (
    <div>
      <Nav
        style={props.style}
        name={cvContent.nav.name}
        email={cvContent.nav.email}
        phone={cvContent.nav.phone}
      />
      <Summary
        title={cvContent.title}
        shortDescription={cvContent.shortDescription}
        summary={cvContent.summary}
      />
      <Experience style={props.style} jobData={cvContent.jobData} />
      <Skills style={props.style} skillData={cvContent.skillData} />
      <SocialSimple style={props.style} />
    </div>
  );
};

Cv.propTypes = {
  style: PropTypes.object,
};
