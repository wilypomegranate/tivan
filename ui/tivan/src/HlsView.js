import React, { Component } from 'react';

import Hls from 'hls.js';

export default class HlsView extends Component {
  render() {
    const videoURL = this.props.videoURL;
    return (
      <div>
        {/* TODO - Need to lookup what this is */}
        <Hls src={videoURL}/>
      </div>
    )
  }
};
