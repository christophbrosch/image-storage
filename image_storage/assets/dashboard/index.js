import React from 'react';
import ReactDOM from "react-dom";

import Button from 'react-bootstrap/Button';
import Component from './javascript/component.js';

function App(){
  return (
    <div>
      <Component></Component>
      <Button variant="primary">
        Hello World!
      </Button>
    </div>
  )
}
