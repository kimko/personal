import React, { Component, useState, useEffect } from "react";
import PropTypes from "prop-types";

import axios from "axios";

import { Nav } from "./nav";
import { Summary } from "./cvSummary";
import { Experience } from "./cvExperience";
import { Skills } from "./cvSkills";
import { SocialSimple } from "./footer";
import { defaultContent } from "./../content/cv";
import { Info } from "./info";

export const Cv = (props) => {
  const [content, setContent] = useState(defaultContent);
  const [showInfo, setShowInfo] = useState(true);
  const [info, setInfo] = useState("Loading data from remote...");
  useEffect(() => {
    (async () => {
      try {
        const response = await axios.get(
          "http://localhost:8004/resumes/public/dflt/",
        );
        setContent(response.data);
        setShowInfo(false);
      } catch (error) {
        // TODO error handling
        console.error(error);
        setInfo("Loading data from remote failed!");
      }
    })();
  }, []);
  return (
    <div>
      {showInfo && <Info message={info} />}
      <Nav
        style={props.style}
        name={content.name}
        email={content.email}
        phone={{ raw: content.phone, pretty: content.phone }}
      />
      <Summary
        title={content.title}
        shortDescription={content.short_description}
        summary={content.summary}
      />
      <Experience style={props.style} jobData={content.jobs} />
      <Skills style={props.style} skillData={content.skills} />
      <SocialSimple style={props.style} />
    </div>
  );
};

Cv.propTypes = {
  style: PropTypes.object,
};
