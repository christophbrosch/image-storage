import React from 'react';

const Component = function(props) {
    
    return (
        <input onClick={function() {alert('click')}} class="form-control mr-sm-5" type="search" placeholder="Search" aria-label="Search">
        </input>
    )
}

export default Component;