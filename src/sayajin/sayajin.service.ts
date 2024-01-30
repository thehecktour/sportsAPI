import { Injectable } from "@nestjs/common";

@Injectable()
export class SayajinService {
    listUsers(){
        return 'Hello';
    }
}