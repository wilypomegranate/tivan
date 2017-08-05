import React, { Component } from 'react';

import ReactHLS from 'react-hls';

export default class HlsView extends Component {
  render() {
    const videoURL = this.props.videoURL;
    return (
      <div>
        {/* TODO - Need to lookup what this is */}
        <ReactHLS url={videoURL} />
      </div>
    )
  }
};

HlsView.propTypes = {
  videoURL: React.PropTypes.string.isRequired
};
