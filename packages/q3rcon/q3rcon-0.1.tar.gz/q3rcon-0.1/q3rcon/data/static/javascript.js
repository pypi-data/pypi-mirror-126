function run(cmd) {
    httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', 'http://localhost:9344/run?' + new URLSearchParams({cmd: cmd}).toString());
    httpRequest.send();
}