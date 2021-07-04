import React from 'react';

const Dataset = (props) => {
    return (
        <div className="col-3 card mx-1">
            <div className="card-body">
                <h4 className="card-title"> { props.name } </h4>
                <h6 className="card-subtitle"> { props.owner } </h6>
                <p className="card-text"> { props.description } </p>
                <a className="card-link" href={ props.delete_url }> Delete </a>
                <a className="card-link" href={ props.detail_url }> Detail </a>
            </div>
        </div>
    )
};

export default Dataset;
