import React, { Component } from 'react';
import HelloWorld from './components/starter/index.jsx';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return <HelloWorld title="Hello from React webpack" />;
  }
}

export default App;
