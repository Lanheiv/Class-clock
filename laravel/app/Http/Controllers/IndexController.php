<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

use App\Http\Controllers\DataRequestController;

class IndexController extends Controller
{
    public function index() {
        return view("index");
    }
    public function request() {
        $dataRequestController = new DataRequestController();
        $chack = $dataRequestController->DataChack();

        $error = [];

        if(!$chack) {
            $dataRequestController->DataCreate();
        }

        $jsonData = Storage::disk('local')->get('json/formatted_data.json');
        if(!$jsonData) {
            $jsonData = Storage::disk("local")->get('json/example.json');
            $error = ["Formatted_data dont exist, using example instead!"];
        }
        $jsonData = json_decode($jsonData, true);

        #return view("index", compact("jsonData", "error"));
    }
}