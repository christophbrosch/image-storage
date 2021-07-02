import React from 'react';
import ListItem from './ListItem';

const Sidebar = function(props) {
    return (
        <div className={(props.phoneMode ? "phone-mode ": "desktop-mode ") + "border-right bg-white col-sm-12 col-lg-3 col-xl-2"} id="sidebar-wrapper">
            <div className="list-group sidebar-heading border-bottom">
                {props.open || props.phoneMode ?
                <span>Start Bootstrap</span>
                :
                <span></span>
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