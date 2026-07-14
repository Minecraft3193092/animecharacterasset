<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}" id="page">

<head>
<title>{{ $pageData['page_content'] }} | wiki</title>
</head>

<style>
.title-s {
    border-bottom: 2px solid #a2a9b1;
}

.wrapper {
    display: flex;
    gap: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

.content {
    flex: 2;
    height: 100%;
    border-radius: 8px;
    background-color: #f4f4f4;
    padding: 20px;
}

.sidebar {
    flex: 1;
    border-radius: 8px;
    background-color: #e5e5e5;
    padding: 20px;
}

.border-2 {
    padding: 10px;
}

.header-text-container {
  text-align: center; 
  border-radius: 8px;
  background-color: #f2f2f2;
  padding: 20px;
}

.footer-text-container {
  text-align: center; 
  border-radius: 8px;
  background-color: #f2f2f2;
  padding: 20px;
}

.nav {
  text-align: center; 
  padding: 10px;
}
</style>

<body>

<header>
<div class="text-container">
 Wiki
</div>
<nav class="nav">
<a href="/mainpage/">{{ __('msg.mainpage') }}</a> | {{ __('msg.welcome', ['name' => $userData->name]) }} | <a href="/login/">{{ __('msg.login') }}</a>
</nav>
</header>

<div class="wrapper">
<main class="content">
<article>
<h1 class="title-s">{{ $page['page_title'] }}</h1>

{{ $page['page_content'] }}
</article>
</main>

<aside class="sidebar">
@yield('sidebar')
</aside>

</div>
<footer>
<div class="border-2">
<div class="footer-text-container">
 Wiki
</div>
</div>
</footer>
</body>