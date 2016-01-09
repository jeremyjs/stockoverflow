import React, {Component} from 'react';

import Graph from './Graph';
import GraphForm from './GraphForm';

export default class Main extends Component {
  render() {
    return (
      <div id='Main'>
        Main
        <Graph />
        <GraphForm />
      </div>
    )
  }
}


