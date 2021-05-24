import React, { Component, useRef, useEffect } from "react";
import PropTypes from "prop-types";

import { defaultContent } from "./../content/cv";

export const CvPlain = (props) => {
  return (
    <div className="ph2 mw7">
      <head>
        <title>CV</title>
      </head>
      <body>
        <h2>{defaultContent.title}</h2>
        <p>{defaultContent.short_description}</p>
        <ul>
          {defaultContent.summary.map((item, idx) => (
            <li key={idx} className="list pv1">
              {"• " + item}
            </li>
          ))}
        </ul>
        <h2>Experience</h2>
        <dl>{processJobData(defaultContent.jobs)}</dl>
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
