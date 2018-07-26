<template>
  <div id="app">
    <nav-bar></nav-bar>
    <message></message>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';
import Message from './components/common/Message.vue';
export default {
  name: 'app',
  components: {Message, NavBar,}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
/**
* Copied from Bootstrap 4
*/
.badge {
    display: inline-block;
    padding: 0.25em 0.4em;
    font-size: 90%;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: 0.25rem;
}

.badge:empty {
    display: none;
}
/**
* Copied from Bootstrap 4
*/
.badge {
    display: inline-block;
    padding: 0.25em 0.4em;
    font-size: 90%;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: 0.25rem;
}

.badge:empty {
    display: none;
}

.badge-pill {
    padding-right: 0.7em;
    padding-left: 0.7em;
    padding-top: 0.3em;
    border-radius: 2.5rem;
}

.badge-primary {
    color: #fff;
    background-color: #007bff;
}

.badge-primary[href]:focus, .badge-primary[href]:hover {
    color: #fff;
    text-decoration: none;
    background-color: #0062cc;
}

.badge-light {
    color: white;
    background-color: #10A0FF;
}

.badge-light[href]:focus, .badge-light[href]:hover {
    color: #212529;
    text-decoration: none;
    background-color: #dae0e5;
}

.badge-dark {
    color: #fff;
    background-color: #343a40;
}

.badge-dark[href]:focus, .badge-dark[href]:hover {
    color: #fff;
    text-decoration: none;
    background-color: #1d2124;
}

/**
* Original styles
*/
.tags-input-default-class {
    padding: .5rem .25rem;

    background: #fff;

    border: 1px solid transparent;
    border-radius: .25rem;
    border-color: #dbdbdb;
}

.tags-input-remove {
    cursor: pointer;
    position: relative;
    display: inline-block;
    width: 0.5rem;
    height: 0.5rem;
    overflow: hidden;
}

.tags-input-remove:before, .tags-input-remove:after {
    content: '';
    position: absolute;
    width: 100%;
    top: 50%;
    left: 0;
    background: white;

    height: 2px;
    margin-top: -1px;
}

.tags-input-remove:before {
    transform: rotate(45deg);
}
.tags-input-remove:after {
    transform: rotate(-45deg);
}

.tags-input input:focus {
    outline: none;
}

.badge-pill {
    padding-right: 0.7em;
    padding-left: 0.7em;
    border-radius: 0.25rem;
}

.badge-primary {
    color: #fff;
    background-color: #007bff;
}

.badge-primary[href]:focus, .badge-primary[href]:hover {
    color: #fff;
    text-decoration: none;
    background-color: #0062cc;
}

.badge-light {
    color: white;
    background-color: #10A0FF;
}

.badge-light[href]:focus, .badge-light[href]:hover {
    color: #212529;
    text-decoration: none;
    background-color: #dae0e5;
}

.badge-dark {
    color: #fff;
    background-color: #343a40;
}

.badge-dark[href]:focus, .badge-dark[href]:hover {
    color: #fff;
    text-decoration: none;
    background-color: #1d2124;
}

/**
* Original styles
*/
.tags-input-default-class {
    padding: .5rem .25rem;
    background: #fff;
    border: 1px solid transparent;
    border-radius: .15rem;
    border-color: #dbdbdb;
}

.tags-input-remove {
    cursor: pointer;
    position: relative;
    display: inline-block;
    width: 0.5rem;
    height: 0.5rem;
    overflow: hidden;
}

.tags-input-remove:before, .tags-input-remove:after {
    content: '';
    position: absolute;
    width: 100%;
    top: 50%;
    left: 0;
    background: white;
    height: 2px;
    margin-top: -1px;
}

.tags-input-remove:before {
    transform: rotate(45deg);
}
.tags-input-remove:after {
    transform: rotate(-45deg);
}

.tags-input input:focus {
    outline: none;
}

.search-bar-container {
    display: flex;
}

.tags-input input {
    font-size: 14px;
}
.search-bar .tags-input input {
    width: 62vw;
}
.container {
    margin: 0;
    max-width: 95vw !important;
    width: 95vw !important;
}

</style>
