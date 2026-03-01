<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\DataRequest;

use Symfony\Component\Process\Process;
use Illuminate\Support\Facades\Storage;
use Symfony\Component\Process\Exception\ProcessFailedException;

class DataRequestController extends Controller
{
    public function request() {
        $error = null;
        $chack = $this->chack();

        if(!$chack) {
            $this->create();
        }

        $jsonData = Storage::disk('local')->get('json/formatted_data.json');
        if(!$jsonData) {
            $jsonData = Storage::disk("local")->get('json/example.json');
            $error = ["Formatted_data dont exist, using example instead!"];
        }
        $jsonData = json_decode($jsonData, true);

        return response()->json([$jsonData, $error]);
    }
    public function chack() {
        $existsToday = DataRequest::whereDate('created_at', now()->toDateString())->exists();

        if(!$existsToday) {
            return false;
        }
        return true;
    }
    public function create() {
        $process = new Process(['python', base_path('../scoper/main.py')], base_path('../'));
        $process->run();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        } else {
            DataRequest::create();
        }
    }
}