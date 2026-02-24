<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class DataRequest extends Model
{
    protected $fillable = [
        'status',
    ];

    const UPDATED_AT = null;
}
