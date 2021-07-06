import React from 'react';
import ReactDOM from 'react-dom';

class FilterableImageList extends React.Component {

    constructor() {
        super();
        this.state = {images: []}
        this.fetchImages()
    };

    fetchImages = () => {
        return fetch(`http://localhost:8000/api/dataset/2/images`)
        .then(res => res.json())
        .then(data => this.setState(state => {
            return state['images'] = data.data
        }))
    };

    render() {
        return (
            <div>
            </div>
        )};
};

ReactDOM.render(
    <FilterableImageList></FilterableImageList>,
    document.getElementById('root')
)