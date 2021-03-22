import React from "react";
import PropTypes from "prop-types";

export const Summary = (props) => {
  return (
    <article className="bb w-100 cf f6 pt5 pl4">
      <div className="flex flex-wrap">
        <div className="w-100 w-third-ns">
          <ShortDescription
            shortDescription={props.shortDescription}
            title={props.title}
          />
        </div>
        <div className="w-100 w-two-thirds-ns pl4-ns">
          <SummaryList summary={props.summary} />
        </div>
      </div>
    </article>
  );
};

Summary.propTypes = {
  shortDescription: PropTypes.string,
  title: PropTypes.string,
  summary: PropTypes.array,
};

const ShortDescription = (props) => {
  return (
    <article className="measure-narrow measure-ns pt2">
      <h1 className="bl bw2 f5 pl1">{props.title}</h1>

      <p className="">{props.shortDescription}</p>
    </article>
  );
};

ShortDescription.propTypes = {
  shortDescription: PropTypes.string,
  title: PropTypes.string,
};

const SummaryList = ({ summary }) => {
  return (
    <article>
      <ul className="pl3 pt4-ns pr2">
        {summary.map((item, idx) => (
          <li key={idx} className="pv1 mw7">
            {item}
          </li>
        ))}
      </ul>
    </article>
  );
};

SummaryList.propTypes = {
  summary: PropTypes.array,
};
