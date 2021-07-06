import React from 'react';

const Image = (props) => {
    return (
        <div className="col-sm-12 col-md-6 col-lg-4 col-xl-2 p-1">
            <img style={{maxWidth: "100%"}} src={props.base_url + props.image_path}></img>
        </div>
    )
};

export default Image;
