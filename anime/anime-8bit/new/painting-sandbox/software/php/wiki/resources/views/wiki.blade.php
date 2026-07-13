<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}" id="page">

<head>
<title>{{ $pageData['page_content'] }} | wiki</title>
</head>

<style>
.wrapper {
    display: flex;
    gap: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

.content {
    flex: 3;
    background-color: #ffffff;
    padding: 20px;
}

.sidebar {
    flex: 1;
    background-color: #f4f4f4;
    padding: 20px;
}
</style>

<body>

<header>
<nav>
  <a href="/mainpage/">{{ __('msg.mainpage') }}</a> | {{ __('msg.welcome', ['name' => $userData->name]) }} | <a href="/login/">{{ __('msg.login') }}</a>
</nav>
</header>

<div class="wrapper">
<main class="content">
<article>
<h1>{{ $page['page_title'] }}</h1>

{{ $page['page_content'] }}
</article>
</main>

<aside class="sidebar">
@yield('sidebar')
</aside>

</div>
<footer>
</footer>
</body>