import React, { Component } from 'react';
import { Form, Dropdown } from 'react-bootstrap';

import HlsView from './HlsView.js';

export default class LiveCameraSelection extends Component {
  render() {
    return (
      <Form>
        {/* TODO - Er? */}
        <Dropdown />
        <HlsView />
      </Form>
    );
  }
};
