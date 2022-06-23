import React, {Component} from 'react';
import {Button, ButtonToolbar, Table} from 'react-bootstrap';
import {AddDepModal} from './AddDepModal';
import {EditDepModal} from './EditDepModal';

export class Department extends Component {

    constructor(props) {
        super(props);
        this.state = {deps: [], addModalShow: false, editModalShow: false}
    }

    refreshList() {
        fetch(process.env.REACT_APP_API + 'department/')
            .then(response => response.json())
            .then(data => {
                this.setState({deps: data});
            });
    }

    componentDidMount() {
        this.refreshList();
    }


    deleteDep(depId) {
        if (window.confirm('Are you sure?')) {
            fetch(process.env.REACT_APP_API + 'department/' + depId + '/', {
                method: 'DELETE',
                header: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            }).then(window.location.reload())

        }
    }

    render() {
        const {deps, depId, depName} = this.state;
        let addModalClose = () => this.setState({addModalShow: false});
        let editModalClose = () => this.setState({editModalShow: false});
        return (
            <div>
                <Table className="mt-4" striped bordered hover size="sm">
                    <thead>
                    <tr>
                        <th>DepartmentId</th>
                        <th>DepartmentName</th>
                        <th>Options</th>
                    </tr>
                    </thead>
                    <tbody>
                    {deps.map(dep =>
                        <tr key={dep.id}>
                            <td>{dep.id}</td>
                            <td>{dep.department_name}</td>
                            <td>
                                <ButtonToolbar>
                                    <Button className="mr-2" variant="info"
                                            onClick={() => this.setState({
                                                editModalShow: true,
                                                depId: dep.id, depName: dep.department_name
                                            })}>
                                        Edit
                                    </Button>

                                    <Button className="mr-2" variant="danger"
                                            onClick={() => this.deleteDep(dep.id)}>
                                        Delete
                                    </Button>

                                    <EditDepModal show={this.state.editModalShow}
                                                  onHide={editModalClose}
                                                  depid={depId}
                                                  depname={depName}/>
                                </ButtonToolbar>

                            </td>

                        </tr>)}
                    </tbody>

                </Table>

                <ButtonToolbar>
                    <Button variant='primary'
                            onClick={() => this.setState({addModalShow: true})}>
                        Add Department</Button>

                    <AddDepModal show={this.state.addModalShow}
                                 onHide={addModalClose}/>
                </ButtonToolbar>
            </div>
        )
    }
}