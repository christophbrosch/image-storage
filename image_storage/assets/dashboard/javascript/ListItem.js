import React from 'react';

const ListItem = function(props) {
return (
        <a className={(!props.phoneMode && !props.open ? "d-flex justify-content-center ": "") + "list-group-item list-group-item-action list-group-item-light p-3"} href={props.url}>
            <i style={{fontSize: "1.5rem"}} className={props.icon}></i> 
            { props.open || props.phoneMode ? 
                <span className="align-bottom pl-3">{props.innerHTML}</span>
            :
                <span></span>
            }
        </a>
    )
}
export default ListItem;








