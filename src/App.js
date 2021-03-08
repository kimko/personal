import React, { Component } from "react";
import { Story } from "./components/story";
import { Nav  } from "./components/nav";
class App extends Component {
  render() {
    return (
      <div>
        <Nav />
        <Story />
      </div>
    );
  }
}

export default App;
