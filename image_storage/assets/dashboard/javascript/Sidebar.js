import React from 'react';
import ListItem from './ListItem';

const Sidebar = function(props) {
    return (
        <div className={(props.open && !props.phoneMode ? "col-lg-2 ": "col-lg-1 ") + "border-right bg-white col-md-12"} id="sidebar-wrapper">
            <div className="list-group sidebar-heading border-bottom">
                {props.open || props.phoneMode ?
                <span>Start Bootstrap</span>
                :
                <span className="text-white"> X </span>
                }
            </div>
            <div className="list-group list-group-flush">
                <ListItem icon="bi bi-bootstrap" innerHTML="Dashboard" open={props.open} phoneMode={props.phoneMode} url={URLS.DASHBOARD}></ListItem>
                <ListItem icon="bi bi-app" innerHTML="About" open={props.open} phoneMode={props.phoneMode} url={URLS.ABOUT}></ListItem>
            </div>
        </div>
    )
}

export default Sidebar;