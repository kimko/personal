import React from "react";
import PropTypes from "prop-types";

export const Skill = (props) => {
  const classn = "f7 b db pa2 link dim ba";
  return (
    <li key={props.skill} className="dib mr1 mb2">
      <div
        className={
          props.main == true ? `${classn}  bg-light-silver` : `${classn} `
        }
      >
        {props.skill}
      </div>
    </li>
  );
};

Skill.propTypes = {
  skill: PropTypes.string,
  main: PropTypes.bool,
};

const processSkillData = (data) => {
  // TODO refactor
  let skills = [];
  let iSkill = 0;
  for (const [skill, value] of Object.entries(data)) {
    iSkill += 100;
    skills.push(<Skill key={skill} main={true} skill={skill} />);
    value.forEach((element, valueIdx) => {
      skills.push(
        <Skill key={iSkill + valueIdx} main={false} skill={element} />,
      );
    });
  }
  return skills;
};

export const Skills = (props) => {
  const skills = processSkillData(props.skillData);
  return (
    <section className="bb w-100 cf pl4" style={props.style}>
      <h1 className="bl bw2 f4 pl1">Technical Skills</h1>
      <ul className="list pl3 pl0-ns pr2">{skills}</ul>
    </section>
  );
};

Skills.propTypes = {
  style: PropTypes.object,
  skillData: PropTypes.object,
};
