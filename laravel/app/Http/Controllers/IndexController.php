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

        $jsonData = Storage::disk("local")->get('json/formatted_data.json');
        if(!$jsonData) {
            $jsonData = Storage::disk("local")->get('json/example.json');
        }

        return view("index");
    }
}