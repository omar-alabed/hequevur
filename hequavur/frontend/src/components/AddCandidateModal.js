import React, {Component} from 'react';
import {Button, Col, Form, Image, Modal, Row} from 'react-bootstrap';

export class AddCandidateModal extends Component {
    photofilename = "anonymous.png";
    imagesrc = process.env.REACT_APP_PHOTOPATH + this.photofilename;

    constructor(props) {
        super(props);
        this.state = {deps: [], selectedFile:''};
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleFileSelected = this.handleFileSelected.bind(this);
    }

    componentDidMount() {
        fetch(process.env.REACT_APP_API + 'department/')
            .then(response => response.json())
            .then(data => {
                this.setState({deps: data});
            });
    }

    handleSubmit(event) {
        event.preventDefault();
        fetch(process.env.REACT_APP_API + 'candidate/create', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                full_name: event.target.CandidateName.value,
                date_of_birth: event.target.DateOfBirth.value,
                years_of_experience: event.target.YearsOfExperience.value,
                department: event.target.Department.value,
                resume: this.state.selectedFile

            })
        })
            .then(res => res.json())
            .then((result) => {
                    window.location.reload()
                },
                (error) => {
                    alert('Failed');
                })
    }


    handleFileSelected(event) {
        event.preventDefault();
        this.setState({selectedFile: event.target.files[0]})

    }

    render() {
        return (
            <div className="container">

                <Modal
                    {...this.props}
                    size="lg"
                    aria-labelledby="contained-modal-title-vcenter"
                    centered
                >
                    <Modal.Header closeButton>
                        <Modal.Title id="contained-modal-title-vcenter">
                            Add Candidate
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>

                        <Row>
                            <Col sm={6}>
                                <Form onSubmit={this.handleSubmit}>
                                    <Form.Group controlId="CandidateName">
                                        <Form.Label>Candidate Name</Form.Label>
                                        <Form.Control type="text" name="CandidateName" required
                                                      placeholder="Candidate Name"/>
                                    </Form.Group>


                                    <Form.Group controlId="DateOfBirth">
                                        <Form.Label>Date Of Birth</Form.Label>
                                        <Form.Control
                                            type="date"
                                            name="DateOfBirth"
                                            required
                                            placeholder="Date Of Birth"
                                        />
                                    </Form.Group>


                                    <Form.Group controlId="YearsOfExperience">
                                        <Form.Label>Years Of Experience</Form.Label>
                                        <Form.Control type="number" name="YearsOfExperience" required
                                                      placeholder="Years Of Experience"/>
                                    </Form.Group>

                                    <Form.Group controlId="Department">
                                        <Form.Label>Department</Form.Label>
                                        <Form.Control as="select">
                                            {this.state.deps.map(dep =>
                                                <option key={dep.id} value={dep.id}>{dep.department_name}</option>)}
                                        </Form.Control>
                                    </Form.Group>



                                    <Form.Group>
                                        <Button variant="primary" type="submit">
                                            Add Candidate
                                        </Button>
                                    </Form.Group>
                                </Form>
                            </Col>

                            <Col sm={6}>
                                <br></br>
                                <h6>Upload your resume here.</h6>
                                <p>Make sure your resume is either in a pdf or docx format, otherwise it will be rejected</p>
                                <br></br>
                                <input onChange={this.handleFileSelected} type="File"/>
                            </Col>
                        </Row>
                    </Modal.Body>

                    <Modal.Footer>
                        <Button variant="danger" onClick={this.props.onHide}>Close</Button>
                    </Modal.Footer>

                </Modal>

            </div>
        )
    }

}