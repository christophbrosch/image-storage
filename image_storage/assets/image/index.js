import React from 'react';
import ReactDOM from 'react-dom';

import Image from './Image';

class FilterableImageList extends React.Component {

    constructor() {
        super();
        this.state = {
            images: [], 
            urls: JSON.parse(document.getElementById('urls').textContent),
            pk: document.getElementById('pk').textContent
        };
        this.fetchImages();
    };

    fetchImages = () => {
        return fetch(`http://localhost:8000/api/dataset/${this.state.pk}/images`)
        .then(res => res.json())
        .then(data => this.setState(state => {
            return state['images'] = data.data;
        }))
    };

    render() {
        return (
            <div>
                <div className="card">
                    <h3 className="card-header">Bilder</h3>
                    <div className="card-body row">
                    { this.state.images.map( image => {
                        return <Image base_url={this.state.urls['image_base']} image_path={image.thumbnail_path}></Image>
                    })}
                    </div>
                </div>
            </div>
        )};
};

ReactDOM.render(
    <FilterableImageList></FilterableImageList>,
    document.getElementById('root')
)