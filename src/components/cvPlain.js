import React, { Component, useRef, useEffect } from "react";
import PropTypes from "prop-types";

import * as cvContent from "./../content/cv";

export const CvPlain = (props) => {
  return (
    <div className="ph2 mw7">
      <head>
        <title>CV</title>
      </head>
      <body>
        <h2>{cvContent.title}</h2>
        <p>{cvContent.shortDescription}</p>
        <ul>
          {cvContent.summary.map((item, idx) => (
            <li key={idx} className="list pv1">
              {"• " + item}
            </li>
          ))}
        </ul>
        <h2>Experience</h2>
        <dl>{processJobData(cvContent.jobData)}</dl>
      </body>
    </div>
  );
};

CvPlain.propTypes = {
  style: PropTypes.object,
};

const processJobData = (data) => {
  // TODO refactor
  let jobs = [];
  let i = 0;
  data.forEach((el, idx) => {
    i += 100;
    jobs.push(
      <dt
        key={idx}
        className="b pv2"
      >{`${el.start}-${el.end} ${el.title} ${el.company}`}</dt>,
    );
    el.experience.forEach((element, idx) => {
      jobs.push(
        <dd key={i + idx} className="pv1">
          {"• " + element.task}
        </dd>,
      );
    });
  });
  return jobs;
};
