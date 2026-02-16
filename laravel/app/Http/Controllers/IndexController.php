<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class IndexController extends Controller
{
    public function index() {
        $time = Storage::disk("local")->get('json/time.json');

        return view("index", compact("time"));
    }
}
