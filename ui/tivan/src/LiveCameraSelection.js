import React, { Component } from 'react';
/* import { Form, Dropdown } from 'react-bootstrap';*/
import { Form } from 'react-bootstrap';

import HlsView from './HlsView.js';

export default class LiveCameraSelection extends Component {
  render() {
    const url = 'http://localhost:8000/ladder/playlist.m3u8';
    return (
      <Form>
        {/* TODO - Er? */}
        {/* <Dropdown /> */}
        <HlsView videoURL={url} />
      </Form>
    );
  }
};
