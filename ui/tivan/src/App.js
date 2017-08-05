import React, {Component} from 'react';
import logo from './logo.svg';

//styles
import './App.less';
import './App.scss';
import './App.styl';
/* import styles from './Modules.css';*/

/* import LiveCameras from './LiveCameras.js';*/
import LiveCameraSelection from './LiveCameraSelection.js'

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo"/>
          <h2 className="App-title"> ☢ custom-react-scripts ☢ </h2>
          <LiveCameraSelection />
        </div>
      </div>
    )
  }
}

export default App;
