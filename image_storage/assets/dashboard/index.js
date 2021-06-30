import React, { useEffect, useState } from 'react';
import ReactDOM from "react-dom";

import Navbar from './javascript/Navbar.js';
import Sidebar from './javascript/Sidebar.js'
import './index.css';

function Navigation(props){

  const [open, setOpen] = useState(true);
  const [phoneMode, setPhoneMode] = useState(false);

  useEffect(() => {
    if (window.outerWidth <= 992) {
      setPhoneMode(true);
    } else {
      setPhoneMode(false);
    };

    window.addEventListener('resize', () => {
      if (window.outerWidth <= 992) {
        setPhoneMode(true);
      } else {
        setPhoneMode(false);
      };
    });
  });

  return (
    <body className={open ? "sb-sidenav-toggled": ""}>
      <div className="d-flex row">
          <Sidebar></Sidebar>
          <div id="content-wrapper" className="col-sm">
              <Navbar open={open} phoneMode={phoneMode} onToggleClick={() => setOpen(!open)}></Navbar>
          </div>
      </div>
    </body>  
  )
};

ReactDOM.render(
  <Navigation></Navigation>,
  document.querySelector('#root')
);
