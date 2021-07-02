import React, { useEffect, useState } from 'react';
import ReactDOM from "react-dom";

import Navbar from './javascript/Navbar.js';
import Sidebar from './javascript/Sidebar.js'
import './index.css';

function Navigation(props){

  const [open, setOpen] = useState(true);
  const [phoneMode, setPhoneMode] = useState(false);


  const handleResize = function() {
    if (window.outerWidth <= 992) {
      setPhoneMode(true);
    } else {
      setPhoneMode(false);
    };
  }
  useEffect(() => {
    handleResize();
    window.addEventListener('resize', () => {
      handleResize();
    });
    return () => {
      window.removeEventListener('resize', handleResize);
    }
  }, []);

  return (
    <div className="d-flex row no-gutters">
        <Sidebar open={open} phoneMode={phoneMode}></Sidebar>
        <div id="content-wrapper" className="col-sm">
            <Navbar open={open} phoneMode={phoneMode} onToggleClick={() => setOpen(!open)}></Navbar>
        </div>
    </div>
  )
};

ReactDOM.render(
  <Navigation></Navigation>,
  document.querySelector('#root')
);
