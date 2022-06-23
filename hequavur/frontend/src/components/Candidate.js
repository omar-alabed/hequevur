import React, {Component} from 'react';
import {Button, ButtonToolbar, Table} from 'react-bootstrap';
import {AddCandidateModal} from './AddCandidateModal';

export class Candidate extends Component {

    constructor(props) {
        super(props);
        this.state = {cands: [], addModalShow: false, editModalShow: false}
    }

    refreshList() {
        let responseStatus = 0
        fetch(process.env.REACT_APP_API + 'candidate/')

            .then(response =>  response.json()
            .then(data => ({status: response.status, body: data})))
            .then(obj => {
                if (obj.status === 200){
                    this.setState({cands: obj.body});
                }
            });
    }

    componentDidMount() {
        this.refreshList();
    }


    render() {
        const {cands} = this.state;
        let addModalClose = () => this.setState({addModalShow: false});
        return (
            <div>
                {cands !== [] &&
                <Table className="mt-4" striped bordered hover size="sm">
                    <thead>
                    <tr>
                        <th>candidate Name</th>
                        <th>Date Of Birth</th>
                        <th>Years Of Experience</th>
                        <th>Department</th>
                    </tr>
                    </thead>
                    <tbody>
                    {cands.map((cand, idx) =>
                        <tr key={idx}>
                            <td>{cand.full_name}</td>
                            <td>{cand.date_of_birth}</td>
                            <td>{cand.years_of_experience}</td>
                            <td>{cand.department}</td>

                        </tr>)}
                    </tbody>

                </Table>
                }
                <ButtonToolbar>
                    <Button variant='primary'
                            onClick={() => this.setState({addModalShow: true})}>
                        Add candidate</Button>

                    <AddCandidateModal show={this.state.addModalShow}
                                       onHide={addModalClose}/>
                </ButtonToolbar>
            </div>
        )
    }
}