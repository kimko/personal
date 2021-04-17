import React, { useRef, useEffect } from "react";
import { HashRouter as Router, Switch, Route, Link } from "react-router-dom";

import { Cv } from "./components/cv";
import { CvPlain } from "./components/cvPlain";
// TODO useContext hook
const style = {
  // color: "#FFFF00",
  // backgroundColor: "#777777",
  color: "#000000",
  backgroundColor: "#CCCCCC",
};

// TODO sectioning headers / article / section

// TODO add analytics and meta tags to html file

function App() {
  const topAnchor = useRef(null);
  useEffect(() => {
    topAnchor.current.focus();
  }, []);
  return (
    <Router>
      <div className="courier" style={style} data-testid="test-div-app">
        <a id="top-anchor" ref={topAnchor} href="#top-anchor" />
        <Switch>
          <Route path="/cv">
            <Cv style={style} />
          </Route>
          <Route path="/plain">
            <CvPlain style={style} />
          </Route>
          <Route path="/">
            <Cv style={style} />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
