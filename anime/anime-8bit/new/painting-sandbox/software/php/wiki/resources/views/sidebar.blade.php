@extends('wiki')

@section('sidebar')
<a href="/page.php?page={{ $page['page_title'] }}">{{ __('msg.view') }}</a>
<a href="/edit.php?page={{ $page['page_title'] }}">{{ __('msg.edit') }}</a>
@endsection