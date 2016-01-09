import React, {Component} from 'react';
import {render} from 'react-dom';
import Sidebar from './Sidebar';
import Main from './Main';

export default class App extends Component {
  render() {
    return (
      <div id='App'>
        App
        <Sidebar />
        <Main />
      </div>
    )
  }
}

render(<App />, document.getElementById('main-container'));
