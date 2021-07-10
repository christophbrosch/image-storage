import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

import { InputGroup, FormControl, Form } from 'react-bootstrap';

import Dataset from './components/Dataset';

class FilterableDatasetList extends React.Component {

    constructor() {
        super();
        this.state = {datasets: JSON.parse(document.getElementById('datasets').textContent), name: '', ownerId: -1, username_mapping: {}}
    };

    componentDidMount = () => {
        // List of unique users
        let unique_user = [... new Set(this.state.datasets.map(dataset => dataset.owner_id))];

        // Fetch the username for each unique user and store it in state
        unique_user.map(user => {
            this.fetchUsername(user).then(
                data => { this.setState((state) => {
                    return state['username_mapping'][user] = data.username;
                })}
            );
        }); 
    };

    fetchUsername = (id) => {
        return fetch(`http://localhost:8000/api/user/${id}/`)
        .then(res => res.json())
    };

    handleChange = ((e) => {
        this.setState((state) => {
            return state[e.target.name] = e.target.value;
        })
    });

    render() {
        return (
            <div>
                <div id="filter" className="row form-group card p-3 bg-white">
                    <h3> Filter </h3>
                    <InputGroup className="mb-3">
                        <FormControl
                            name="name" // This is e.target.name
                            placeholder="Name"
                            aria-label="Name"
                            onChange={this.handleChange}
                        />
                    </InputGroup>
                    <InputGroup>
                        <Form.Control
                            name="ownerId"
                            as="select"
                            onChange={this.handleChange}
                            >
                            <option value={-1}>None</option>
                            {this.state.datasets.map(dataset => {
                                return <option value={dataset.owner_id}>{this.state.username_mapping[dataset.owner_id]}</option>
                            })}
                        </Form.Control>
                    </InputGroup>
                </div>
                <div className="row mt-4">
                    { this.state.datasets
                        .filter( dataset => dataset.name.includes(this.state.name) 
                                            && ( dataset.owner_id == this.state.ownerId || this.state.ownerId == -1 ))
                        .map( dataset => {
                            return <Dataset name={dataset.name} 
                                            owner={this.state.username_mapping[dataset.owner_id]} 
                                            description={dataset.description} 
                                            detail_url={dataset.detail_url} 
                                            delete_url={dataset.delete_url} />  
                    })}
                </div>
            </div>
        )};
};

ReactDOM.render(
    <FilterableDatasetList></FilterableDatasetList>,
    document.getElementById('root')
)