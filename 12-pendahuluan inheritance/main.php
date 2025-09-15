<?php 

// CONTOH DI PHP

class Hero 
{
    public $name;
    public $health;
    public function __construct($name, $health) 
    {
        $this->name = $name;
        $this->health = $health;
    }
};

class HeroFighter extends Hero
{
    public function __construct($name, $health) 
    {
        parent::__construct($name, $health);
    }
};

$alucard = new HeroFighter("alucard", 1000);

var_dump([
    'name' => $alucard->name,
    'health' => $alucard->health,
]);