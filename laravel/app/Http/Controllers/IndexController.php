<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

use App\Http\Controllers\DataRequestController;

class IndexController extends Controller
{
    public function index() {
        $dataRequestController = new DataRequestController();
        $chack = $dataRequestController->DataChack();

        if(!$chack) {
            $dataRequestController->DataCreate();
        }

        return view("index");
    }
}
