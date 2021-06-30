import React from 'react';

const Sidebar = function() {
    return (
        <div className="border-right bg-white col-sm-12 col-lg-3 col-xl-2" id="sidebar-wrapper">
            <div className="list-group sidebar-heading border-bottom">
                Start Bootstrap
            </div>
            <div className="list-group list-group-flush">
                <a className="list-group-item list-group-item-action list-group-item-light p-3" href="#!">Dashboard</a>
                <a className="list-group-item list-group-item-action list-group-item-light p-3" href="#!">Shortcuts</a>
                <a className="list-group-item list-group-item-action list-group-item-light p-3" href="#!">Overview</a>
                <a className="list-group-item list-group-item-action list-group-item-light p-3" href="#!">Events</a>
                <a className="list-group-item list-group-item-action list-group-item-light p-3" href="#!">Profile</a>
                <a className="list-group-item list-group-item-action list-group-item-light p-3" href="#!">Status</a>
            </div>
        </div>
    )
}

export default Sidebar;