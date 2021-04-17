import React from "react";
import PropTypes from "prop-types";

export const Task = (props) => {
  const classn = `f7 near-black ttl pr1 dib ba b--dotted mr1 tracked-tight
        bg-animate hover-bg-gray hover-near-black`;
  return (
    <li className="pb2 mw6">
      <div>
        <span className="mr1">{props.task}</span>
        {props.tools.map((item, idx) => (
          <span key={idx} className={`${classn}`}>
            {item}
          </span>
        ))}
      </div>
    </li>
  );
};

Task.propTypes = {
  task: PropTypes.string,
  tools: PropTypes.array,
};

export const Job = (props) => {
  return (
    <article className="pt2 f6">
      <div className="flex flex-wrap">
        <div className="w-100 w-third-ns">
          <h1 className="cf f6 mv1">
            <time className="fl" dateTime="2018-07">
              {props.job.start}
            </time>
            <span className="fl ph1">-</span>
            <time className="fl" dateTime="2021-03">
              {props.job.end}
            </time>
          </h1>
          <div className="fl f6">{props.job.location}</div>
        </div>
        <div className="w-100 w-two-thirds-ns pl4-ns">
          <h1 className=" f6 mv1 pr2">
            <span className="">{props.job.title}</span>
            <span className="f7 ph1">-</span>
            <span className="f7">{props.job.company}</span>
          </h1>
          <ul className="pl3 pr2 mt0">
            {props.job.experience.map((item, idx) => (
              <Task key={idx} task={item.task} tools={item.tools} />
            ))}
          </ul>
        </div>
      </div>
    </article>
  );
};

Job.propTypes = {
  job: PropTypes.object,
};

export const Experience = (props) => {
  return (
    <section
      className="bb w-100 cf pl4 pb2"
      style={props.style}
      data-testid="test-section-experience"
    >
      <div className="flex flex-wrap">
        <div className="w-100 w-third-ns">
          <h1 className="bl bw2 f5 pl1">Experience</h1>
        </div>
      </div>
      {props.jobData.map((job, idx) => (
        <Job key={idx} style={props.style} job={job} />
      ))}
    </section>
  );
};

Experience.propTypes = {
  style: PropTypes.object,
  jobData: PropTypes.array,
};
