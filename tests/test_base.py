import pytest
import tests.common as common
import nomad


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT)
    return n


# integration tests requires nomad Vagrant VM or Binary running
def test_base_get_connection_error():
    n = nomad.Nomad(
        host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.evaluations["nope"]


def test_base_put_connection_error():
    n = nomad.Nomad(
        host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.system.initiate_garbage_collection()


def test_base_delete_connection_error():
    n = nomad.Nomad(
        host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.job.deregister_job("example")

def test_base_get_params():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, region="global")
    url = n.requester._endpointBuilder('jobs')
    r = n.requester.get(url, params={'key': 'value'})
    assert r.status_code == 200

def test_base_get_no_params():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, region="global")
    url = n.requester._endpointBuilder('jobs')
    r = n.requester.get(url)
    assert r.status_code == 200

def test_base_post_no_params():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, region="global")
    url = n.requester._endpointBuilder('job', 'example', 'evaluate')
    r = n.requester.post(url)
    assert r.status_code == 200

def test_base_post_dict_params():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, region="global")
    url = n.requester._endpointBuilder('job', 'example', 'evaluate')
    r = n.requester.post(url, params={'key': 'value'})
    assert r.status_code == 200

def test_base_post_string_params():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, region="global")
    url = n.requester._endpointBuilder('job', 'example', 'evaluate')
    r = n.requester.post(url, params="key=value")
    assert r.status_code == 200
