import React, {Component} from 'react';

import SearchBar from './SearchBar';
import Portfolio from './Portfolio';

export default class Sidebar extends Component {
  render() {
    return (
      <div id='Sidebar'>
        Sidebar
        <SearchBar />
        <Portfolio />
      </div>
    )
  }
}


