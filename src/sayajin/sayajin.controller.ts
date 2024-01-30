import { Controller, Get } from "@nestjs/common";

@Controller('users')
export class SayajinController {
    @Get()
    listUsers(){
        return 'Usuarios';
    }
}